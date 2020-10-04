%global packname  RIA
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Radiomics Image Analysis Toolbox for Medial Images

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nat >= 1.8.11
BuildRequires:    R-CRAN-oro.nifti >= 0.9.1
BuildRequires:    R-CRAN-oro.dicom >= 0.5.0
Requires:         R-CRAN-nat >= 1.8.11
Requires:         R-CRAN-oro.nifti >= 0.9.1
Requires:         R-CRAN-oro.dicom >= 0.5.0

%description
Radiomics image analysis toolbox for 2D and 3D radiological images. RIA
supports DICOM, NIfTI and nrrd file formats. RIA calculates first-order,
gray level co-occurrence matrix, gray level run length matrix and
geometry-based statistics. Almost all calculations are done using
vectorized formulas to optimize run speeds. Calculation of several
thousands of parameters only takes minutes on a single core of a
conventional PC.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
