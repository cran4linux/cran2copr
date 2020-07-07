%global packname  mand
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Multivariate Analysis for Neuroimaging Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-msma 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-oro.dicom 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-msma 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-oro.dicom 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-caret 

%description
Several functions can be used to analyze neuroimaging data using
multivariate methods based on the 'msma' package. For more details, please
see Kawaguchi et al. (2017) <doi:10.1093/biostatistics/kxx011> and
Kawaguchi (2019) <DOI:10.5772/intechopen.80531>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
