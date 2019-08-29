%global packname  colormap
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Color Palettes using Colormaps Node Module

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 

%description
Allows to generate colors from palettes defined in the colormap module of
'Node.js'. (see <https://github.com/bpostlethwaite/colormap> for more
information). In total it provides 44 distinct palettes made from
sequential and/or diverging colors. In addition to the pre defined
palettes you can also specify your own set of colors. There are also scale
functions that can be used with 'ggplot2'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/js
%{rlibdir}/%{packname}/INDEX
