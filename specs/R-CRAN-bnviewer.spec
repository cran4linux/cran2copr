%global __brp_check_rpaths %{nil}
%global packname  bnviewer
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Networks Interactive Visualization and Explainable Artificial Intelligence

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn >= 4.3
BuildRequires:    R-CRAN-visNetwork >= 2.0.4
BuildRequires:    R-CRAN-igraph >= 1.2.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-graphics 
Requires:         R-CRAN-bnlearn >= 4.3
Requires:         R-CRAN-visNetwork >= 2.0.4
Requires:         R-CRAN-igraph >= 1.2.4
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 
Requires:         R-graphics 

%description
Bayesian networks provide an intuitive framework for probabilistic
reasoning and its graphical nature can be interpreted quite clearly. Graph
based methods of machine learning are becoming more popular because they
offer a richer model of knowledge that can be understood by a human in a
graphical format. The 'bnviewer' is an R Package that allows the
interactive visualization of Bayesian Networks. The aim of this package is
to improve the Bayesian Networks visualization over the basic and static
views offered by existing packages.

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
