%global __brp_check_rpaths %{nil}
%global packname  RTCC
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
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
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
