%global packname  RTCC
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Detecting Trait Clustering in Environmental Gradients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-Rcpp 

%description
The Randomized Trait Community Clustering method (Triado-Margarit et al.,
2019, <doi:10.1038/s41396-019-0454-4>) is a statistical approach which
allows to determine whether if an observed trait clustering pattern is
related to an increasing environmental constrain. The method 1) determines
whether exists or not a trait clustering on the sampled communities and 2)
assess if the observed clustering signal is related or not to an
increasing environmental constrain along an environmental gradient. Also,
when the effect of the environmental gradient is not linear, allows to
determine consistent thresholds on the community assembly based on
trait-values.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
