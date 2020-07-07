%global packname  Sojourn.Data
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Supporting Objects for Sojourn Accelerometer Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-nnet 
Requires:         R-CRAN-caret 
Requires:         R-nnet 

%description
Stores objects (e.g. neural networks) that are needed for using Sojourn
accelerometer methods. For more information, see Lyden K, Keadle S,
Staudenmayer J, & Freedson P (2014) <doi:10.1249/MSS.0b013e3182a42a2d>,
Ellingson LD, Schwabacher IJ, Kim Y, Welk GJ, & Cook DB (2016)
<doi:10.1249/MSS.0000000000000915>, and Hibbing PR, Ellingson LD, Dixon
PM, & Welk GJ (2018) <doi:10.1249/MSS.0000000000001486>.

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
%{rlibdir}/%{packname}/INDEX
