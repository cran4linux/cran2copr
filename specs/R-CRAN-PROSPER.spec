%global packname  PROSPER
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          2%{?dist}%{?buildtag}
Summary:          Simulation of Weed Population Dynamics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-data.table 

%description
An environment to simulate the development of annual plant populations
with regard to population dynamics and genetics, especially herbicide
resistance. It combines genetics on the individual level (Renton et al.
2011) with a stochastic development on the population level (Daedlow,
2015). Renton, M, Diggle, A, Manalil, S and Powles, S (2011)
<doi:10.1016/j.jtbi.2011.05.010> Daedlow, Daniel (2015, doctoral
dissertation: University of Rostock, Faculty of Agriculture and
Environmental Sciences.)

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
