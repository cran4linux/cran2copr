%global __brp_check_rpaths %{nil}
%global packname  findviews
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          A View Generator for Multidimensional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-grid 

%description
A tool to explore wide data sets, by detecting, ranking and plotting
groups of statistically dependent columns.

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
