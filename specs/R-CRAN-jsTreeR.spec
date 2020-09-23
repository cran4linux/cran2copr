%global packname  jsTreeR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Wrapper of the JavaScript Library 'jsTree'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-utils 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-miniUI 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-CRAN-base64enc 
Requires:         R-utils 

%description
Creates interactive trees that can be included in 'Shiny' apps and R
markdown documents. A tree allows to represent hierarchical data (e.g. the
contents of a directory). Similar to the 'shinyTree' package but offers
more features and options, such as the grid extension, restricting the
drag-and-drop behavior, and settings for the search functionality. It is
possible to attach some data to the nodes of a tree and then to get these
data in 'Shiny' when a node is selected. Also provides a 'Shiny' gadget
allowing to manipulate one or more folders.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
