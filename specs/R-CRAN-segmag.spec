%global __brp_check_rpaths %{nil}
%global packname  segmag
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Determine Event Boundaries in Event Segmentation Experiments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-plyr 

%description
Contains functions that help to determine event boundaries in event
segmentation experiments by bootstrapping a critical segmentation
magnitude under the null hypothesis that all key presses were randomly
distributed across the experiment. Segmentation magnitude is defined as
the sum of Gaussians centered at the times of the segmentation key presses
performed by the participants. Within a participant, the maximum of the
overlaid Gaussians is used to prevent an excessive influence of a single
participant on the overall outcome (e.g. if a participant is pressing the
key multiple times in succession). Further functions are included, such as
plotting the results.

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
