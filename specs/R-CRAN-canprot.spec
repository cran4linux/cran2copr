%global __brp_check_rpaths %{nil}
%global packname  canprot
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Chemical Metrics of Differentially Expressed Proteins

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CHNOSZ >= 1.3.2
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-CHNOSZ >= 1.3.2
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rmarkdown 

%description
Chemical metrics of differentially expressed proteins in cancer and cell
culture proteomics experiments. Data files in the package have amino acid
compositions of proteins obtained from UniProt and >250 published lists of
up- and down-regulated proteins in different cancer types and laboratory
experiments. Functions are provided to calculate chemical metrics
including protein length, grand average of hydropathicity (GRAVY),
isoelectric point (pI), carbon oxidation state, and stoichiometric
hydration state; the latter two are described in Dick et al. (2020)
<doi:10.5194/bg-17-6145-2020>. The vignettes visualize differences of
chemical metrics between up- and down-regulated proteins and list
literature references for all datasets.

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
