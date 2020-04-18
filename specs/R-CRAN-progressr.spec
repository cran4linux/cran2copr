%global packname  progressr
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          A Inclusive, Unifying API for Progress Updates

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-utils 
Requires:         R-CRAN-digest 
Requires:         R-utils 

%description
A minimal, unifying API for scripts and packages to report progress
updates from anywhere including when using parallel processing.  The
package is designed such that the developer can to focus on what progress
should be reported on without having to worry about how to present it.
The end user has full control of how, where, and when to render these
progress updates, e.g. in the terminal using utils::txtProgressBar() or
progress::progress_bar(), in a graphical user interface using
utils::winProgressBar(), tcltk::tkProgressBar() or shiny::withProgress(),
via the speakers using beep::beepr(), or on a file system via the size of
a file. Anyone can add additional, customized, progression handlers. The
'progressr' package uses R's condition framework for signaling progress
updated. Because of this, progress can be reported from almost anywhere in
R, e.g. from classical for and while loops, from map-reduce APIs like the
lapply() family of functions, 'purrr', 'plyr', and 'foreach'. It will also
work with parallel processing via the 'future' framework, e.g.
future.apply::future_lapply(), furrr::future_map(), and 'foreach' with
'doFuture'. The package is compatible with Shiny applications.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
