%global packname  SNPassoc
%global packver   2.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          SNPs-Based Whole Genome Association Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haplo.stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-poisbinom 
Requires:         R-CRAN-haplo.stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-survival 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-poisbinom 

%description
Functions to perform most of the common analysis in genome association
studies are implemented. These analyses include descriptive statistics and
exploratory analysis of missing values, calculation of Hardy-Weinberg
equilibrium, analysis of association based on generalized linear models
(either for quantitative or binary traits), and analysis of multiple SNPs
(haplotype and epistasis analysis). Permutation test and related tests
(sum statistic and truncated product) are also implemented. Max-statistic
and genetic risk-allele score exact distributions are also possible to be
estimated. The methods are described in Gonzalez JR et al. (2007) <doi:
10.1093/bioinformatics/btm025>.

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
