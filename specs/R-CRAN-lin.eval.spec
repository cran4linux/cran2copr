%global __brp_check_rpaths %{nil}
%global packname  lin.eval
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Perform Polynomial Evaluation of Linearity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
Requires:         R-CRAN-broom 

%description
Evaluates whether the relationship between two vectors is linear or
nonlinear. Performs a test to determine how well a linear model fits the
data compared to higher order polynomial models. Jhang et al. (2004)
<doi:10.1043/1543-2165(2004)128%3C44:EOLITC%3E2.0.CO;2>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
