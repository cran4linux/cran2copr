%global packname  causact
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Accelerated Bayesian Analytics with DAGs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-igraph >= 1.2.5
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.6
BuildRequires:    R-CRAN-tidyr >= 1.0.3
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-greta >= 0.3.1
BuildRequires:    R-CRAN-coda >= 0.19.3
BuildRequires:    R-CRAN-rstudioapi >= 0.11
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-htmlwidgets >= 1.5.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-igraph >= 1.2.5
Requires:         R-CRAN-DiagrammeR >= 1.0.6
Requires:         R-CRAN-tidyr >= 1.0.3
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-greta >= 0.3.1
Requires:         R-CRAN-coda >= 0.19.3
Requires:         R-CRAN-rstudioapi >= 0.11

%description
Accelerate Bayesian analytics workflows in 'R' through interactive
modelling, visualization, and inference. Define probabilistic graphical
models using directed acyclic graphs (DAGs) as a unifying language for
business stakeholders, statisticians, and programmers. This package relies
on the sleek and elegant 'greta' package for Bayesian inference. 'greta',
in turn, is an interface into 'TensorFlow' from 'R'. Install 'greta' using
instructions available here:
<http://www.causact.com/install-tensorflow-greta-and-causact.html>. See
<http://github.com/flyaflya/causact> or <http://causact.com> for more
documentation.

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
