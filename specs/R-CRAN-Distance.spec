%global packname  Distance
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Distance Sampling Detection Function and Abundance Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mrds >= 2.2.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-mrds >= 2.2.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 

%description
A simple way of fitting detection functions to distance sampling data for
both line and point transects. Adjustment term selection, left and right
truncation as well as monotonicity constraints and binning are supported.
Abundance and density estimates can also be calculated (via a
Horvitz-Thompson-like estimator) if survey area information is provided.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/minke.xlsx
%{rlibdir}/%{packname}/INDEX
