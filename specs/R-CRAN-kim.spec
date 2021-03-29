%global packname  kim
%global packver   0.2.172
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.172
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Behavioral Science Researchers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-interactions 
BuildRequires:    R-CRAN-lemon 
BuildRequires:    R-CRAN-lm.beta 
BuildRequires:    R-CRAN-mediation 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-paran 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-WRS2 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-effsize 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-interactions 
Requires:         R-CRAN-lemon 
Requires:         R-CRAN-lm.beta 
Requires:         R-CRAN-mediation 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-paran 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-WRS2 

%description
Miscellaneous functions to simplify and expedite analyses of experimental
data. Examples include a function that plots sample means of groups in a
factorial experimental design, a function that conducts robust regressions
with bootstrapped samples, and a function that conducts robust two-way
analysis of variance. Selected References: Canty & Ripley (2021)
<https://CRAN.R-project.org/package=boot>. Cohen (1988)
<doi:10.4324/9780203771587>. Dinno (2018)
<https://CRAN.R-project.org/package=paran>. Dowle et al. (2021)
<https://CRAN.R-project.org/package=data.table>. Edwards et al. (2020)
<https://CRAN.R-project.org/package=lemon>. Fox et al. (2020)
<https://CRAN.R-project.org/package=car>. Hester et al. (2020)
<https://CRAN.R-project.org/package=remotes>. Ioannidis (2005)
<doi:10.1371/journal.pmed.0020124> Kim (2021)
<doi:10.5281/zenodo.4641436>. Kim (2020)
<https://CRAN.R-project.org/package=ezr>. Long (2020)
<https://CRAN.R-project.org/package=interactions>. Mair & Wilcox (2021)
<https://CRAN.R-project.org/package=WRS2>. Pasek et al. (2020)
<https://CRAN.R-project.org/package=weights>. Simmons et al. (2011)
<doi:10.1177/0956797611417632>. Tingley et al. (2019)
<https://CRAN.R-project.org/package=mediation>. Torchiano (2020)
<https://CRAN.R-project.org/package=effsize>. Wickham et al. (2020)
<https://CRAN.R-project.org/package=ggplot2>. Wilke (2021)
<https://CRAN.R-project.org/package=ggridges>.

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
