%global packname  jmdem
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Fitting Joint Mean and Dispersion Effects Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-statmod 

%description
Joint mean and dispersion effects models fit the mean and dispersion
parameters of a response variable by two separate linear models, the mean
and dispersion submodels, simultaneously. It also allows the users to
choose either the deviance or the Pearson residuals as the response
variable of the dispersion submodel. Furthermore, the package provides the
possibility to nest the submodels in one another, if one of the parameters
has significant explanatory power on the other. Wu & Li (2016)
<doi:10.1016/j.csda.2016.04.015>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
