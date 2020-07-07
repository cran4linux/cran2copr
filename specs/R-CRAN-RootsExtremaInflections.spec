%global packname  RootsExtremaInflections
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}
Summary:          Finds Roots, Extrema and Inflection Points of a Curve

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-inflection 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-inflection 

%description
Implementation of Taylor Regression Estimator (TRE), Tulip Extreme Finding
Estimator (TEFE), Bell Extreme Finding Estimator (BEFE), Integration
Extreme Finding Estimator (IEFE) and Integration Root Finding Estimator
(IRFE) for roots, extrema and inflections of a curve . Christopoulos, DT
(2019) <doi:10.13140/RG.2.2.17158.32324> . Christopoulos, DT (2016)
<doi:10.2139/ssrn.3043076> . Christopoulos, DT (2016)
<https://veltech.edu.in/wp-content/uploads/2016/04/Paper-04-2016.pdf> .
Christopoulos, DT (2014) <arXiv:1206.5478v2 [math.NA]> .

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
