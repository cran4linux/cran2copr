%global packname  nixmass
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Snow Water Equivalent Modeling with the 'Delta.snow' Model andEmpirical Regression Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lubridate 
Requires:         R-grDevices 

%description
Snow water equivalent is modeled with the process based 'delta.snow' model
and empirical regression models using relationships between density and
diverse at-site parameters. The methods are described in Winkler et al.
(2020) <doi:10.5194/hess-2020-152>, Guyennon et al. (2019)
<doi:10.1016/j.coldregions.2019.102859>, Pistocchi (2016)
<doi:10.1016/j.ejrh.2016.03.004>, Jonas et al. (2009)
<doi:10.1016/j.jhydrol.2009.09.021> and Sturm et al. (2010)
<doi:10.1175/2010JHM1202.1>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
