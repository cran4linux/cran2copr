%global packname  Copula.Markov.survival
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Copula Markov Model with Dependent Censoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-graphics 

%description
Perform likelihood estimation and corresponding analysis under the
copula-based Markov chain model for serially dependent event times with a
dependent terminal event. A two stage estimation method is applied for
estimating model parameters. Two copula functions are used for measuring
dependence. One is used for modeling serial dependence in recurrent event
times. The other one is for modeling dependent censoring. The baseline
hazard functions are modeled by the Weibull distributions. See Huang
(2019)
<https://etd.lib.nctu.edu.tw/cgi-bin/gs32/ncugsweb.cgi?o=dncucdr&s=id=%22GC106225601%22.&searchmode=basic>
for detail.

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
