Summary:	GNUstep Suite
Summary(pl.UTF-8):   Środowisko GNUstep
Name:		metapackage-gnustep
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Desktop
Requires:	Affiche
Requires:	Backbone
Requires:	GWorkspace
Requires:	WindowMaker
Requires:	gnustep-base
Requires:	gnustep-examples
Requires:	gnustep-gui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUstep suite metapackage.

%description -l pl.UTF-8
Metapakiet środowiska GNUstep.

%files
