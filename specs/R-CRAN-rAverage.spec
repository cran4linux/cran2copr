%global __brp_check_rpaths %{nil}
%global packname  rAverage
%global packver   0.5-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          3%{?dist}%{?buildtag}
Summary:          Parameter Estimation for the Averaging Model of InformationIntegration Theory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8
Requires:         R-core >= 2.8
BuildRequires:    R-methods 
BuildRequires:    R-tcltk 
Requires:         R-methods 
Requires:         R-tcltk 

%description
Implementation of the R-Average method for parameter estimation of
averaging models of the Anderson's Information Integration Theory by
Vidotto, G., Massidda, D., & Noventa, S. (2010)
<https://www.uv.es/psicologica/articulos3FM.10/3Vidotto.pdf>.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/libs
