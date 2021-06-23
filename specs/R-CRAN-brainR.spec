%global __brp_check_rpaths %{nil}
%global packname  brainR
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          3%{?dist}%{?buildtag}
Summary:          Helper Functions to 'misc3d' and 'rgl' Packages for BrainImaging

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-misc3d 
Requires:         R-CRAN-oro.nifti 
Requires:         R-grDevices 

%description
This includes functions for creating 3D and 4D images using 'WebGL',
'rgl', and 'JavaScript' commands. This package relies on the X toolkit
('XTK', <https://github.com/xtk/X#readme>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/index_template.html
%doc %{rlibdir}/%{packname}/MNI152_T1_1mm_brain.nii.gz
%doc %{rlibdir}/%{packname}/MNI152_T1_2mm_brain.nii.gz
%doc %{rlibdir}/%{packname}/MNI152_T1_4mm_brain.nii.gz
%doc %{rlibdir}/%{packname}/MNI152_T1_8mm_brain.nii.gz
%doc %{rlibdir}/%{packname}/my_embed_template.html
%doc %{rlibdir}/%{packname}/my_template.html
%doc %{rlibdir}/%{packname}/Visit_1_2mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_1_8mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_1.nii.gz
%doc %{rlibdir}/%{packname}/Visit_2_2mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_2_8mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_2.nii.gz
%doc %{rlibdir}/%{packname}/Visit_3_2mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_3_8mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_3.nii.gz
%doc %{rlibdir}/%{packname}/Visit_4_2mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_4_8mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_4.nii.gz
%doc %{rlibdir}/%{packname}/Visit_5_2mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_5_8mm.nii.gz
%doc %{rlibdir}/%{packname}/Visit_5.nii.gz
%doc %{rlibdir}/%{packname}/xtk_edge.js
%doc %{rlibdir}/%{packname}/xtk_xdat.gui.js
%{rlibdir}/%{packname}/INDEX
