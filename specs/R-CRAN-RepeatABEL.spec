%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RepeatABEL
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          GWAS for Multiple Observations on Related Individuals

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hglm 
BuildRequires:    R-methods 
Requires:         R-CRAN-hglm 
Requires:         R-methods 

%description
Performs genome-wide association studies (GWAS) on individuals that are
both related and have repeated measurements. For each Single Nucleotide
Polymorphism (SNP), it computes score statistic based p-values for a
linear mixed model including random polygenic effects and a random effect
for repeated measurements. The computed p-values can be visualized in a
Manhattan plot. For more details see Ronnegard et al. (2016)
<doi:10.1111/2041-210X.12535> and for more examples see
<https://github.com/larsronn/RepeatABEL_Tutorials>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
