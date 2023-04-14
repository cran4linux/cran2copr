%global __brp_check_rpaths %{nil}
%global packname  nat.nblast
%global packver   1.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          3%{?dist}%{?buildtag}
Summary:          NeuroAnatomy Toolbox ('nat') Extension for Assessing NeuronSimilarity and Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-nat >= 1.5.12
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-dendroextras 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-spam 
Requires:         R-CRAN-nat >= 1.5.12
Requires:         R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-dendroextras 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-spam 

%description
Extends package 'nat' (NeuroAnatomy Toolbox) by providing a collection of
NBLAST-related functions for neuronal morphology comparison (Costa et al.
(2016) <doi: 10.1016/j.neuron.2016.06.012>).

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
