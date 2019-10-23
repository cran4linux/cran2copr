%global packname  TukeyRegion
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Tukey Region and Median

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-ddalpha 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-bfp 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-ddalpha 
Requires:         R-MASS 
Requires:         R-CRAN-bfp 
Requires:         R-CRAN-Rglpk 

%description
Tukey regions are polytopes in the Euclidean space, viz. upper-level sets
of the Tukey depth function on given data. The bordering hyperplanes of a
Tukey region are computed as well as its vertices, facets, centroid, and
volume. In addition, the Tukey median set, which is the non-empty Tukey
region having highest depth level, and its barycenter (= Tukey median) are
calculated. Tukey regions are visualized in dimension two and three. For
details see Liu, Mosler, and Mozharovskyi (2017) <arXiv:1412.5122>. See
file LICENSE.note for additional license information.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
