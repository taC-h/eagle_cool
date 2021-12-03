from typing import List,  overload, Optional, Dict, Any
from dataclasses import asdict
from ._util import get, post, dict2query, reject_none
from ._types import Color, URLItem, PathItem
from requests import Response

class Eagle():
    def __init__(self, * , schema="http://", domain="localhost", port="41595"):
        self._url_base = f"{schema}{domain}:{port}/api"
    
    #APPLICSTION
    def application_info(self) -> Response:
        return get(self._url_base + "/application/info")
    
    #FOLDER
    @overload
    def folder_create(self, *, json: dict) -> Response:
        ...
    @overload
    def folder_create(self, folderName: str , parent: str) -> Response:
        ...
    
    def folder_create(
        self, *,
        json: Optional[dict]=None,
        folderName: Optional[str]=None,
        parent: Optional[str]=None,
    ) -> Response:
        json = json or reject_none({
            "folderName": folderName,
            "parent": parent,
        })
        return post(self._url_base + "/folder/create", json=json)
    
    @overload
    def folder_rename(self, *, json: dict) -> Response:
        ...
    @overload
    def folder_rename(self, *, filderId: str, folderName: str) -> Response:
        ...
    
    def folder_rename(
        self, *,
        json: Optional[dict]=None,
        folderId: Optional[str]=None,
        folderName: Optional[str]=None,
    ) -> Response:
        json = json or reject_none({
            "folderId": folderId,
            "folderName": folderName,
        })
        return post(self._url_base + "/folder/rename", json=json)
    
    @overload
    def folder_update(self, *, json: dict) -> Response:
        ...
    @overload
    def folder_update(self, folderId: str, newName: str, newDescription: str, newColor: Color) -> Response:
        ...
    
    def folder_update(self, *,
        json: Optional[dict]=None,
        folderId: Optional[str]=None,
        newName: Optional[str]=None,
        newDescription: Optional[str]=None,
        newColor: Optional[Color]=None,
    ) -> Response:
        json = json or reject_none({
            "folderId": folderId,
            "newName": newName,
            "newDescription": newDescription,
            "newColor": newColor
        })
        return post(self._url_base + "/folder/update", json=json)
    
    def folder_list(self) -> Response:
        return get(self._url_base + "/folder/list")

    def folder_listRecent(self) -> Response:
        return get(self._url_base + "/folder/listRecent")
    
    #ITEM
    @overload
    def item_addFromURL(self, *, josn: dict) -> Response:
        ...
    @overload
    def item_addFromURL(self, *,
        url: str,
        name: str,
        website: Optional[str],
        tags: Optional[List[str]],
        annotation: Optional[str],
        modificationTime: Optional[int],
        folderId: Optional[str],
        headers: Optional[dict],
    ) -> Response:
        ...
    
    def item_addFromURL(
        self, *,
        json: Optional[dict]=None,
        url: Optional[str]=None,
        name: Optional[str]=None,
        website: Optional[str]=None,
        tags: Optional[List[str]]=None,
        annotation: Optional[str]=None,
        modificationTime: Optional[int]=None,
        folderId: Optional[str]=None,
        headers: Optional[dict]=None,
    ) -> Response:
        json = json or reject_none({
            "url": url,
            "name": name,
            "website": website,
            "tags": tags,
            "annotation": annotation,
            "modificationTime": modificationTime,
            "folderId": folderId,
            "headers": headers,
        })
        return post(self._url_base + "/item/addFromURL", json=json)
    
    @overload
    def item_addFromURLs(self, *, json: dict) -> Response:
        ...
    @overload
    def item_addFromURLs(self, *, items: List[URLItem], folderId: Optional[str]) -> Response:
        ...
    
    def item_addFromURLs(
        self, *,
        json: Optional[dict]=None,
        items: Optional[List[URLItem]]=None,
        folderId: Optional[str]=None,
    ) -> Response:
        json = json or reject_none({
            "items": [asdict(item) for item in items],
            "folderId": folderId,
        })
        return post(self._url_base + "/item/addFromURLs", json=json)
    
    @overload
    def item_addFromPath(self, *, json: dict) -> Response:
        ...
    @overload
    def item_addFromPath(
        self, *,
        path: str,
        name: str,
        website: Optional[str],
        annotation: Optional[str],
        tags: Optional[List[str]],
        folderId: Optional[str],
    ) -> Response:
        ...
    
    def item_addFromPath(
        self, *,
        json: Optional[dict]=None,
        path: Optional[str]=None,
        name: Optional[str]=None,
        website: Optional[str]=None,
        annotation: Optional[str]=None,
        tags: Optional[List[str]]=None,
        folderId: Optional[str]=None,
    ) -> Response:
        json = json or reject_none({
            "path": path,
            "name": name,
            "website": website,
            "annotation": annotation,
            "tags": tags,
            "folderId": folderId,
        })
        return post(self._url_base + "/item/addFromPath", json=json)
    
    @overload
    def item_addFromPaths(self, *, json: dict) -> Response:
        ...
    @overload
    def item_addFromPaths(self, *, items: List[PathItem], folderId: Optional[str]) -> Response:
        ...
    
    def item_addFromPaths(
        self, *,
        json: Optional[dict]=None,
        items: Optional[List[PathItem]]=None,
        folderId: Optional[str]=None,
        ) -> Response:
        json = json or reject_none({
            "items": [asdict(item) for item in items],
            "folderId": folderId,
        })
        return post(self._url_base + "/item/addFromPaths", json=json)
    
    @overload
    def item_addBookmark(self, *, json: dict) -> Response:
        ...
    @overload
    def item_addBookmark(
        self, *,
        url: str,
        name: str,
        base64: Optional[str],
        tags: Optional[List[str]],
        modificationTime: Optional[int],
        folderId: Optional[str],
    ) -> Response:
        ...
    
    def item_addBookmark(
        self, *,
        json: Optional[dict]=None,
        url: Optional[str]=None,
        name: Optional[str]=None,
        base64: Optional[str]=None,
        tags: Optional[List[str]]=None,
        modificationTime: Optional[int]=None,
        folderId: Optional[str]=None,
    ) -> Response:
        json = json or reject_none({
            "url": url,
            "name": name,
            "base64": base64,
            "tags": tags,
            "modificationTime": modificationTime,
            "folderId": folderId
        })
        return post(self._url_base + "/item/addBookmark")
    
    def item_info(self, param: Optional[dict[str,str]]=None) -> Response:
        return get(self._url_base + f"/item/info{ dict2query(param) }")
    
    def item_thumbnail(self, param: Optional[dict[str,str]]=None) -> Response:
        return get(self._url_base + f"/item/thumbnail{ dict2query(param) }")
    
    def item_list(self, param: Optional[dict[str,str]]=None) -> Response:
        return get(self._url_base + f"/item/list{ dict2query(param) }")
    
    @overload
    def item_refreshPalette(self, *, json: dict) -> Response:
        ...
    @overload
    def item_refreshPalette(self, *, id: str) -> Response:
        ...
    
    def item_refreshPalette(
        self, *,
        json: Optional[dict]=None,
        id: Optional[str]=None
    ) -> Response:
        json = json or {
            "id": id
        }
        return post(self._url_base + "/item/refreshPalette", json=json)
    
    @overload
    def item_refreshThumbnail(self, *, json: dict) -> Response:
        ...
    @overload
    def item_refreshThumbnail(self, *, id: str) -> Response:
        ...
    
    def item_refreshThumbnail(
        self, *,
        json: Optional[dict]=None,
        id: Optional[str]=None
    ) -> Response:
        json = json or {
            "id": id
        }
        return post(self._url_base + "/item/refreshThumbnail", json=json)
    
    @overload
    def item_update(self, *, json: dict) -> Response:
        ...
    @overload
    def item_update(
        self, *,
        id: str,
        tags: Optional[List[str]],
        annotation: Optional[str],
        url: Optional[str],
        star: Optional[int]
    ) -> Response:
        ...
    
    def item_update(
        self, *,
        json: Optional[dict]=None,
        id: str=None,
        tags: Optional[List[str]]=None,
        annotation: Optional[str]=None,
        url: Optional[str]=None,
        star: Optional[int]=None,
    ) -> Response:
        json = json or reject_none({
            "id": id,
            "tags": tags,
            "annotation": annotation,
            "url": url,
            "star": star
        })
        return post(self._url_base + "/item/update", json=json)
    
    #LIBRARY
    def library_info(self) -> Response:
        return get(self._url_base + "/library/info")
    
    def library_history(self) -> Response:
        return get(self._url_base + "/library/history")
    
    @overload
    def library_switch(self, *, json: dict) -> Response:
        ...
    @overload
    def library_switch(self, *, libraryPath: str) -> Response:
        ...
    def library_switch(
        self, *,
        json: Optional[dict]=None,
        libraryPath: Optional[str]=None,
    ) -> Response:
        json = json or {
            "libraryPath": libraryPath
        }
        return post(self._url_base + "/library/switch", json=json)
