%global packname  DiceOptim
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}%{?buildtag}
Summary:          Kriging-Based Optimization for Computer Experiments

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-DiceKriging >= 1.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-DiceDesign 
Requires:         R-CRAN-DiceKriging >= 1.2
Requires:         R-methods 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-DiceDesign 

%description
Efficient Global Optimization (EGO) algorithm as described in "Roustant et
al. (2012)" <doi:10.18637/jss.v051.i01> and adaptations for problems with
noise ("Picheny and Ginsbourger, 2012") <doi:10.1016/j.csda.2013.03.018>,
parallel infill, and problems with constraints.

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
