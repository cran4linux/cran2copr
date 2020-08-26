%global packname  SNPassoc
%global packver   1.9-2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          SNPs-based Whole Genome Association Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haplo.stats 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
Requires:         R-CRAN-haplo.stats 
Requires:         R-survival 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 

%description
This package carries out most common analysis when performing whole genome
association studies. These analyses include descriptive statistics and
exploratory analysis of missing values, calculation of Hardy-Weinberg
equilibrium, analysis of association based on generalized linear models
(either for quantitative or binary traits), and analysis of multiple SNPs
(haplotype and epistasis analysis). Permutation test and related tests
(sum statistic and truncated product) are also implemented. Max-statistic
and genetic risk-allele score exact distributions are also possible to be
estimated.

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
