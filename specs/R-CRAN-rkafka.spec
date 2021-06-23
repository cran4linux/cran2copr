%global __brp_check_rpaths %{nil}
%global packname  rkafka
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Using Apache 'Kafka' Messaging Queue Through 'R'

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-RUnit 
BuildRequires:    R-CRAN-rkafkajars 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-RUnit 
Requires:         R-CRAN-rkafkajars 

%description
Apache 'Kafka' is an open-source message broker project developed by the
Apache Software Foundation which can be thought of as a distributed,
partitioned, replicated commit log service.At a high level, producers send
messages over the network to the 'Kafka' cluster which in turn serves them
up to consumers.See <http://kafka.apache.org/> for more
information.Functions included in this package enable:1.Creating 'Kafka'
producer 2.Writing messages to a topic 3.Closing 'Kafka' producer
4.Creating 'Kafka' consumer 5.Reading messages from a topic 6.Closing
'Kafka' consumer. The jars required for this package are included in a
separate package 'rkafkajars'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NOTICE
%{rlibdir}/%{packname}/INDEX
