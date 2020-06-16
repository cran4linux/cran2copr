%global packname  rEDM
%global packver   1.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8
Release:          2%{?dist}
Summary:          Empirical Dynamic Modeling ('EDM')

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-methods 

%description
An implementation of 'EDM' algorithms based on research software developed
for internal use at the Sugihara Lab ('UCSD/SIO').  The package is
implemented with 'Rcpp' wrappers around the 'cppEDM' library.  It
implements the 'simplex' projection method from Sugihara & May (1990)
<doi:10.1038/344734a0>, the 'S-map' algorithm from Sugihara (1994)
<doi:10.1098/rsta.1994.0106>, convergent cross mapping described in
Sugihara et al. (2012) <doi:10.1126/science.1227079>, and, 'multiview
embedding' described in Ye & Sugihara (2016)
<doi:10.1126/science.aag0863>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs