%global __brp_check_rpaths %{nil}
%global packname  ARIbrain
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          All-Resolution Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hommel 
BuildRequires:    R-CRAN-RNifti 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-hommel 
Requires:         R-CRAN-RNifti 
Requires:         R-CRAN-plyr 

%description
It performs All-Resolutions Inference (ARI) on functional Magnetic
Resonance Image (fMRI) data. As a main feature, it estimates lower bounds
for the proportion of active voxels in a set of clusters as, for example,
given by a cluster-wise analysis. The method is described in Rosenblatt,
Finos, Weeda, Solari, Goeman (2018)
<doi:10.1016/j.neuroimage.2018.07.060>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
