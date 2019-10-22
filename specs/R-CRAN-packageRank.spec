%global packname  packageRank
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
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
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-cranlogs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-RCurl 

%description
Compute and visualize the cross-sectional and longitudinal number and rank
percentile of package downloads from RStudio's CRAN mirror.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
