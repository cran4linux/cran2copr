%global __brp_check_rpaths %{nil}
%global packname  toolStability
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tool for Stability Indices Calculation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-nortest 
Requires:         R-stats 

%description
Tools to calculate stability indices with parametric, non-parametric and
probabilistic approaches. The basic data format requirement for
'toolStability' is a data frame with 3 columns including numeric trait
values, genotype,and environmental labels. Output format of each function
is the dataframe with chosen stability index for each genotype. Function
"table_stability" offers the summary table of all stability indices in
this package. Sample dataset in this package is from: Casadebaig P, Zheng
B, Chapman S et al. (2016) <doi: 10.1371/journal.pone.0146385>. Indices
used in this package are from: Döring TF, Reckling M (2018) <doi:
10.1016/j.eja.2018.06.007>. Eberhart SA, Russell WA (1966) <doi:
10.2135/cropsci1966.0011183X000600010011x>. Eskridge KM (1990) <doi:
10.2135/cropsci1990.0011183X003000020025x>. Finlay KW, Wilkinson GN (1963)
<doi: 10.1071/AR9630742>. Hanson WD (1970) Genotypic stability. <doi:
10.1007/BF00285245>. Lin CS, Binns MR (1988)
<https://cdnsciencepub.com/doi/abs/10.4141/cjps88-018>. Nassar R, Hühn M
(1987). Pinthus MJ (1973) <doi: 10.1007/BF00021563>. Römer T (1917).
Shukla GK (1972). Wricke G (1962).

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
