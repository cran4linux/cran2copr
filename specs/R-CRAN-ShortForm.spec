%global packname  ShortForm
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          2%{?dist}%{?buildtag}
Summary:          Automatic Short Form Creation

License:          LGPL (>= 2.0, < 3) | Mozilla Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.5.22
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-lavaan >= 0.5.22
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 

%description
Performs automatic creation of short forms of scales with an ant colony
optimization algorithm and a Tabu search. As implemented in the package,
the ant colony algorithm randomly selects items to build a model of a
specified length, then updates the probability of item selection according
to the fit of the best model within each set of searches. The algorithm
continues until the same items are selected by multiple ants a given
number of times in a row. On the other hand, the Tabu search changes one
parameter at a time to be either free, constrained, or fixed while keeping
track of the changes made and putting changes that result in worse fit in
a "tabu" list so that the algorithm does not revisit them for some number
of searches. See Leite, Huang, & Marcoulides (2008)
<doi:10.1080/00273170802285743> for an applied example of the ant colony
algorithm, and Marcoulides & Falk (2018)
<doi:10.1080/10705511.2017.1409074> for an applied example of the Tabu
search.

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
