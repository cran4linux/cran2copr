%global packname  qMRI
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Methods for Quantitative Magnetic Resonance Imaging ('qMRI')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-aws >= 2.2
BuildRequires:    R-CRAN-dti >= 1.4
BuildRequires:    R-CRAN-awsMethods >= 1.0
BuildRequires:    R-CRAN-oro.nifti >= 0.9
BuildRequires:    R-CRAN-adimpro >= 0.9
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-aws >= 2.2
Requires:         R-CRAN-dti >= 1.4
Requires:         R-CRAN-awsMethods >= 1.0
Requires:         R-CRAN-oro.nifti >= 0.9
Requires:         R-CRAN-adimpro >= 0.9
Requires:         R-CRAN-stringr 

%description
Implementation of methods for estimation of quantitative maps from
Multi-Parameter Mapping (MPM) acquisitions (Weiskopf et al. (2013)
<doi:10.3389/fnins.2013.00095>) including adaptive smoothing methods in
the framework of the ESTATICS model (Estimating the apparent transverse
relaxation time (R2*) from images with different contrasts, Weiskopf et
al. (2014) <doi:10.3389/fnins.2014.00278>). The smoothing method is
described in Mohammadi et al. (2017). <doi:10.20347/WIAS.PREPRINT.2432>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
