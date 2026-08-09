%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BKMutate
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis of Induced Mutagenesis Experiments in Crop Plants

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 

%description
A colour-first toolkit for the statistical analysis of induced mutagenesis
experiments in crop plants. It fits dose-response models to physical and
chemical mutagen data and estimates the median lethal and growth-reduction
doses (LD50, GR50) with confidence intervals obtained from Fieller's
theorem; quantifies first-generation biological damage (lethality, injury
and pollen sterility); and estimates mutagenic effectiveness and mutagenic
efficiency. Effectiveness and efficiency are conventionally reported as
point estimates only; this package treats them as functions of binomial
proportions and supplies interval estimates by the delta method on the
logarithmic scale and by the nonparametric bootstrap. It further provides
chlorophyll mutation spectrum analysis with tests of homogeneity and
diversity, generalised linear models for second-generation mutant counts
with formal assessment of overdispersion, and formal comparison of
mutagens including relative biological effectiveness. Every analysis
returns a tidy result object and a publication-ready 'ggplot2' figure.
Methods follow Konzak et al. (1965, ISBN:9789201150653), Fieller (1954)
<doi:10.1111/j.2517-6161.1954.tb00159.x> and Katz et al. (1978)
<doi:10.2307/2530610>.

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
