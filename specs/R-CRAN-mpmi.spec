%global packname  mpmi
%global packver   0.43.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.43.1
Release:          3%{?dist}%{?buildtag}
Summary:          Mixed-Pair Mutual Information Estimators

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.2
Requires:         R-core >= 3.6.2
BuildRequires:    R-KernSmooth 
Requires:         R-KernSmooth 

%description
Uses a kernel smoothing approach to calculate Mutual Information for
comparisons between all types of variables including continuous vs
continuous, continuous vs discrete and discrete vs discrete. Uses a
nonparametric bias correction giving Bias Corrected Mutual Information
(BCMI). Implemented efficiently in Fortran 95 with OpenMP and suited to
large genomic datasets.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
