%global packname  MBC
%global packver   0.10-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.4
Release:          3%{?dist}
Summary:          Multivariate Bias Correction of Climate Model Outputs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-energy 
Requires:         R-Matrix 
Requires:         R-CRAN-energy 

%description
Calibrate and apply multivariate bias correction algorithms for climate
model simulations of multiple climate variables. Three methods described
by Cannon (2016) <doi:10.1175/JCLI-D-15-0679.1> and Cannon (2018)
<doi:10.1007/s00382-017-3580-6> are implemented: (i) MBC Pearson
correlation (MBCp), (ii) MBC rank correlation (MBCr), and (iii) MBC
N-dimensional PDF transform (MBCn).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
