%global packname  canprot
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Analysis of Differentially Expressed Proteins in Cancer

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rmarkdown 

%description
Compositional analysis of differentially expressed proteins in cancer and
cell culture proteomics experiments. The data include lists of up- and
down-regulated proteins in different cancer types (breast, colorectal,
liver, lung, pancreatic, prostate) and laboratory conditions (hypoxia,
hyperosmotic stress, high glucose, 3D cell culture, and proteins secreted
in hypoxia), together with amino acid compositions computed for protein
sequences obtained from UniProt. Functions are provided to calculate
compositional metrics including protein length, carbon oxidation state,
and stoichiometric hydration state. In addition, phylostrata (evolutionary
ages) of protein-coding genes are compiled using data from Liebeskind et
al. (2016) <doi:10.1093/gbe/evw113> or Trigos et al. (2017)
<doi:10.1073/pnas.1617743114>. The vignettes contain plots of
compositional differences, phylostrata for human proteins, and references
for all datasets.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
