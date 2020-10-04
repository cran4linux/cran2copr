%global packname  userfriendlyscience
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          2%{?dist}%{?buildtag}
Summary:          Quantitative Analysis Made Accessible

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ufs >= 0.0.1
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-SCRT 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-ufs >= 0.0.1
Requires:         R-CRAN-BiasedUrn 
Requires:         R-CRAN-car 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-SCRT 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xtable 

%description
Contains a number of functions that serve two goals. First, to make R more
accessible to people migrating from SPSS by adding a number of functions
that behave roughly like their SPSS equivalents (also see
<https://rosettastats.com>). Second, to make a number of slightly more
advanced functions more user friendly to relatively novice users. The
package also conveniently houses a number of additional functions that are
intended to increase the quality of methodology and statistics in
psychology, not by offering technical solutions, but by shifting
perspectives, for example towards reasoning based on sampling
distributions as opposed to on point estimates.

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

%files
%{rlibdir}/%{packname}
