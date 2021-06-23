%global __brp_check_rpaths %{nil}
%global packname  SmoothWin
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Soft Windowing on Linear Regression

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-Rfast 
Requires:         R-nlme 
Requires:         R-CRAN-Rfast 

%description
The main function in the package utilizes a windowing function in the form
of an exponential weighting function to linear models. The bandwidth and
sharpness of the window are controlled by two parameters. Then, a series
of tests are used to identify the right parameters of the window (see
Hamed Haselimashhadi et al (2019)
<https://www.biorxiv.org/content/10.1101/656678v1>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
