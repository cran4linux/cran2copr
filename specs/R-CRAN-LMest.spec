%global packname  LMest
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Latent Markov Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mclust >= 5.4.6
BuildRequires:    R-grDevices >= 4.0.2
BuildRequires:    R-CRAN-diagram >= 1.6.4
BuildRequires:    R-CRAN-Formula >= 1.2.3
BuildRequires:    R-CRAN-scatterplot3d >= 0.3.41
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MultiLCIRT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mmm 
BuildRequires:    R-CRAN-mix 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-mclust >= 5.4.6
Requires:         R-grDevices >= 4.0.2
Requires:         R-CRAN-diagram >= 1.6.4
Requires:         R-CRAN-Formula >= 1.2.3
Requires:         R-CRAN-scatterplot3d >= 0.3.41
Requires:         R-MASS 
Requires:         R-CRAN-MultiLCIRT 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mmm 
Requires:         R-CRAN-mix 
Requires:         R-utils 
Requires:         R-graphics 

%description
Latent Markov models for longitudinal continuous and categorical data. See
Bartolucci, Pandolfi, Pennoni (2017)<doi:10.18637/jss.v081.i04>.

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
