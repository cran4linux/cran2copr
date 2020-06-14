%global packname  packageRank
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          2%{?dist}
Summary:          Computation and Visualization of Package Download Counts andPercentiles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-cranlogs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-pkgsearch 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-rversions 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-cranlogs 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-pkgsearch 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-rversions 
Requires:         R-stats 

%description
Compute and visualize the cross-sectional and longitudinal number and rank
percentile of package downloads from RStudio's CRAN mirror.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
