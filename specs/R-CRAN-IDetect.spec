%global __brp_check_rpaths %{nil}
%global packname  IDetect
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Isolate-Detect Methodology for Multiple Change-Point Detection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-splines 
Requires:         R-splines 

%description
Provides efficient implementation of the Isolate-Detect methodology for
the consistent estimation of the number and location of multiple
change-points in one-dimensional data sequences from the "deterministic +
noise" model. For details on the Isolate-Detect methodology, please see
Anastasiou and Fryzlewicz (2018)
<https://docs.wixstatic.com/ugd/24cdcc_6a0866c574654163b8255e272bc0001b.pdf>.
Currently implemented scenarios are: piecewise-constant signal with
Gaussian noise, piecewise-constant signal with heavy-tailed noise,
continuous piecewise-linear signal with Gaussian noise, continuous
piecewise-linear signal with heavy-tailed noise.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
