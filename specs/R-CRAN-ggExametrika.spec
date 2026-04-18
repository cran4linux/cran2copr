%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggExametrika
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of 'exametrika' Output Using 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tidyr 

%description
Provides 'ggplot2'-based visualization functions for output objects from
the 'exametrika' package, which implements test data engineering methods
described in Shojima (2022, ISBN:978-981-16-9547-1). Supports a wide range
of psychometric models including Item Response Theory, Latent Class
Analysis, Latent Rank Analysis, Biclustering (binary, ordinal, and
nominal), Bayesian Network Models, and related network models. All plot
functions return 'ggplot2' objects that can be further customized by the
user.

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
