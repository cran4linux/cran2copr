%global __brp_check_rpaths %{nil}
%global packname  textgRid
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Praat TextGrid Objects in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
The software application Praat can be used to annotate waveform data
(e.g., to mark intervals of interest or to label events). (See
<http://www.fon.hum.uva.nl/praat/> for more information about Praat.)
These annotations are stored in a Praat TextGrid object, which consists of
a number of interval tiers and point tiers. An interval tier consists of
sequential (i.e., not overlapping) labeled intervals. A point tier
consists of labeled events that have no duration. The 'textgRid' package
provides S4 classes, generics, and methods for accessing information that
is stored in Praat TextGrid objects.

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
