%global __brp_check_rpaths %{nil}
%global packname  esmisc
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Misc Functions of Eduard Szöcs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readr 

%description
Misc functions programmed by Eduard Szöcs. Provides read_regnie() to read
gridded precipitation data from German Weather Service (DWD, see
<http://www.dwd.de/> for more information).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
