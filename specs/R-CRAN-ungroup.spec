%global packname  ungroup
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          2%{?dist}
Summary:          Penalized Composite Link Model for Efficient Estimation ofSmooth Distributions from Coarsely Binned Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-MortalitySmooth >= 2.3.4
BuildRequires:    R-CRAN-pbapply >= 1.3
BuildRequires:    R-CRAN-rgl >= 0.99.0
BuildRequires:    R-CRAN-Rdpack >= 0.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-MortalitySmooth >= 2.3.4
Requires:         R-CRAN-pbapply >= 1.3
Requires:         R-CRAN-rgl >= 0.99.0
Requires:         R-CRAN-Rdpack >= 0.8
Requires:         R-CRAN-Rcpp >= 0.12.0

%description
Versatile method for ungrouping histograms (binned count data) assuming
that counts are Poisson distributed and that the underlying sequence on a
fine grid to be estimated is smooth. The method is based on the composite
link model and estimation is achieved by maximizing a penalized
likelihood. Smooth detailed sequences of counts and rates are so estimated
from the binned counts. Ungrouping binned data can be desirable for many
reasons: Bins can be too coarse to allow for accurate analysis;
comparisons can be hindered when different grouping approaches are used in
different histograms; and the last interval is often wide and open-ended
and, thus, covers a lot of information in the tail area. Age-at-death
distributions grouped in age classes and abridged life tables are examples
of binned data. Because of modest assumptions, the approach is suitable
for many demographic and epidemiological applications. For a detailed
description of the method and applications see Rizzi et al. (2015)
<doi:10.1093/aje/kwv020>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figures
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
