%global packname  vampyr
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Factor Analysis Controlling the Effects of Response Bias

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimbase 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-EFA.MRFA 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-PCovR 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-fungible 
BuildRequires:    R-CRAN-semPlot 
Requires:         R-stats 
Requires:         R-CRAN-optimbase 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-EFA.MRFA 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-PCovR 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-fungible 
Requires:         R-CRAN-semPlot 

%description
Vampirize the response biases from a dataset! Performs factor analysis
controlling the effects of social desirability and acquiescence using the
method described in Ferrando, Lorenzo-Seva & Chico (2009)
<doi:10.1080/10705510902751374>.

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
