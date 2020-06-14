%global packname  oasis
%global packver   3.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.4
Release:          2%{?dist}
Summary:          Multiple Sclerosis Lesion Segmentation using Magnetic ResonanceImaging (MRI)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fslr >= 2.13
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-mmand 
Requires:         R-CRAN-fslr >= 2.13
Requires:         R-CRAN-neurobase 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-mmand 

%description
Trains and makes predictions from the OASIS method, described in detail in
the paper "OASIS is Automated Statistical Inference for Segmentation, with
applications to multiple sclerosis lesion segmentation in MRI"
<doi:10.1016/j.nicl.2013.03.002>. OASIS is a method for multiple sclerosis
(MS) lesion segmentation on structural magnetic resonance image (MRI)
studies. OASIS creates probability maps of lesion presence using the
FLAIR, T2, T1, and PD structural MRI volumes. This packages allows for
training of the OASIS model and prediction of OASIS probability maps from
a trained model with user supplied studies that have a gold standard
lesion segmentation masks. The package will also create OASIS probability
maps for MRI studies using the OASIS model from the OASIS paper if no gold
standard lesion segmentation masks are available.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
