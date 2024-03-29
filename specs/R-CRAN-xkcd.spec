%global __brp_check_rpaths %{nil}
%global packname  xkcd
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Plotting ggplot2 Graphics in an XKCD Style

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 

%description
Plotting ggplot2 graphs using the XKCD style.

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
